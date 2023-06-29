from fastapi import status

class UserResponse:
    
    USER_CREATED = {
        'status': status.HTTP_201_CREATED,
        'key': 'created',
        'message': "User Created"
    }
    
    USER_NOT_CREATED = {
        'status': status.HTTP_409_CONFLICT,
        'key': 'id',
        'message': 'User is Not Created'
    }
    
    USER_ALREADY_EXISTS = {
        'status': status.HTTP_409_CONFLICT,
        'key': 'email',
        'message': "Email is already taken"
    }
    
    USER_NOT_FOUND = {
        'status': status.HTTP_404_NOT_FOUND,
        'key': 'id',
        'message': 'User Not Found'
    }
    
    USER_DELETED = {
        'status': status.HTTP_200_OK,
        'key': 'id',
        'message': 'User Deleted'
    }
    
class UserObjectResponse:
    
    OBJECT_NOT_FOUND = {
        'status': status.HTTP_404_NOT_FOUND,
        'key': 'owner_id',
        'message': 'Object Not Found'
    }
    
    OBJECT_NOT_DELETED = {
        'status': status.HTTP_400_BAD_REQUEST,
        'key': 'owner_id',
        'message': 'Object Not Deleted'
    }