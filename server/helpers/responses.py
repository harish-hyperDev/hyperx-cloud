from fastapi import status

class UserResponse:
    
    USER_CREATED = {
        'status': status.HTTP_201_CREATED,
        'key': 'created',
        'message': "User Created"
    }
    
    USER_ALREADY_EXISTS = {
        'status': status.HTTP_409_CONFLICT,
        'key': 'email',
        'message': "Email is already taken"
    }
    
    USER_NOT_FOUND = {
        'status': status.HTTP_404_NOT_FOUND,
        'key': '_id',
        'message': 'User Not Found'
    }
    