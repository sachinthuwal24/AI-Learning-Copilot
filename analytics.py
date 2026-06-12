import pandas as pd
import matplotlib.pyplot as plt

def create_chart(data):

    df = pd.DataFrame(
        data,
        columns=["ID","Topic","Score"]
    )

    return df