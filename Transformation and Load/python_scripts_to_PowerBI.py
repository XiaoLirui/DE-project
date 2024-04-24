import pandas as pd
from rockset import RocksetClient

# create RocksetClient object
rs = RocksetClient(api_key='DlF5OiV4ghhJQuQLvcJuEeXciTMZUz0cbwY93BCRHzQ7XOwuZKLuvSy5V8cpJ64E')

try:
    res = rs.Queries.query(
        sql={
            "query": "SELECT data FROM commons.de_project limit 10",
        }
    )

    data1 = [item['data'] for item in res.results]

    df = pd.DataFrame(data1)
    print(df)

except rockset.ApiException as e:
    print("Exception when querying: %s\n" % e)
