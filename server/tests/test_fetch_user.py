from actions.UserActions import UserActions
from models.model import UserModel

def test_fetch():
    result = UserActions.get(email="test@aloha.com")
    
    print(result)
    # assert result == UserResponse.CREATED