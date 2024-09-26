import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> list[int]:
    #return [players.shape[0], lplayers.shape[1]]
    return [len(players), len(players.columns)]