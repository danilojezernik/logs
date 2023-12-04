from src.domain.admin.user import User

user = [
    User(
        username='danijezernik',
        email='dani.jezernik@gmail.com',
        full_name='Danilo Jezernik',
        hashed_password='$2b$12$Hf0FSLvF3JXsdnMFzFqKoeKOMCYNvlWyoGkFnbmiMqR2Byva6UziC',
        disabled=False
    ).dict(by_alias=True)
]
