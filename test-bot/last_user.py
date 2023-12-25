class LastUser:
    user_id = None

    def __init__(self, user_id) -> None:
        LastUser.user_id = user_id

    @staticmethod
    def get_last_user_id():
        return LastUser.user_id
