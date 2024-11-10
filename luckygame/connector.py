from connectDB import cursor, conn
id = None
obj = None


def saver(user_id: int, sample) -> None:
    """
    This function places the parameters it receives in two global variables
    :param user_id:
    :param sample:
    :return: None
    """
    global id, obj
    id = user_id
    obj = sample


def update_game() -> None:
    """
    This function updates the target game using the values pointed to by the global variables

    :return: None
    """
    # print("update game")

    global id, obj
    user_id = id
    sample = obj
    # print(user_id, sample.myScore)

    # Updating the selected record in the table of games
    cursor.execute(
        "UPDATE games SET chance_box = ?, score = ?, total_boxes = ?, mojeze = ?, gold_coin = ? "
        "WHERE user_id = ?",
        (sample.myChanceBox, sample.myScore, sample.total_boxes, sample.mojeze, sample.GoldCoin, user_id)
    )
    # save the information
    conn.commit()