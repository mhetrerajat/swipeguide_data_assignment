from datetime import datetime

import pandas as pd
from slugify import slugify
import click
import distance
from datetime import datetime, timedelta

from app.storage_manager import StorageManager


class Recommender(object):
    def __init__(self, path):
        self.path = path

    def _read(self, path=None):
        """Fetches data with the help of StorageManager and creates DataFrame
        
        Arguments:
            path {str} -- Path of JSON file
        
        Returns:
            df -- Data of JSON file as a DataFrame
        """

        path = path if path else self.path

        storage = StorageManager(path)
        df = pd.DataFrame([x for x in storage.fetch()])
        return df

    def clean(self, df):
        """Does preprocessing on data
        
        Arguments:
            df {pandas.DataFrame} -- Data loaded as dataframe
        
        Returns:
            df {pandas.DataFrame} -- Preprocessed data
        """
        # Change data types as per necessity
        df = df.astype({'timestamp': int})

        # Add date column using timestamp
        df['date'] = df.apply(lambda x: datetime.fromtimestamp(x.timestamp),
                              axis=1)

        # Add slugified content column to remove duplicates, case mismatches
        df['clean_content'] = df.apply(lambda x: slugify(x.content,
                                                         separator='|'),
                                       axis=1)

        # Sort data by date
        df = df.sort_values('date', ascending=True)
        return df

    def get(self):
        """Processes data and calculate recommended tags for url
        
        Returns:
            recommendations {pandas.DataFrame} -- recommended tags for urls
        """

        # Read data
        df = self._read(self.path)

        # Clean data
        df = self.clean(df)

        # User level events count
        user_events_count = df.groupby(
            by=['user_id', 'event_type']).nunique().id.unstack()

        page_views_df = df.query('event_type == "pageview"')

        recommendations = []
        last_page_views = {}
        default_page_view_time = datetime(1970, 1, 1)
        for idx, row in page_views_df.iterrows():
            user_id = row.user_id
            page_view_time = row.date

            last_page_view = last_page_views.get(user_id,
                                                 default_page_view_time)

            threshold_time = max(page_view_time - timedelta(minutes=30),
                                 last_page_view)
            last_page_views.update({user_id: page_view_time})

            _df = df.query(
                'user_id == @user_id & event_type == "search" & date >= @threshold_time & date <= @page_view_time'
            )
            if _df.shape[0]:
                mdf = pd.merge(_df, _df.shift(1), on=_df.index)
                mdf.fillna(value='', inplace=True)
                f = lambda x: distance.nlevenshtein(x.content_x, x.content_y)
                mdf['distance'] = mdf.apply(f, axis=1)
                result = mdf.query('content_y != "" & distance > 0.6')
                tags = result.content_y.tolist()
                if tags:
                    recommendations.append({
                        'url': row.url,
                        'tags': ",".join(tags)
                    })

        recommendations = pd.DataFrame(recommendations)
        return recommendations
