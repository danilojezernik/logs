from src.domain.user import User

user_dict = [
    User(
        username='danijezernik',
        email='dani.jezernik@gmail.com',
        full_name='Danilo Jezernik',
        hashed_password='$2b$12$Hf0FSLvF3JXsdnMFzFqKoeKOMCYNvlWyoGkFnbmiMqR2Byva6UziC',
        disabled=False
    ).dict(by_alias=True)
]
