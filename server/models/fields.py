from pydantic import Field



class UserFields:
    name = Field(
        description="Name of the user",
        example="John Smith"
    )
    email = Field(
        description="Email address of the user",
        example="john@example.com"
    )
    password = Field(
        description="Password of the user"
    )
    type = Field(
        description="User type of the user",
        example="free-tier"     # free-tier, paid
    )
    data_limit = Field(
        description="Data limit allocated for the user type",
        example="30.0"
    )
    # Write an put opertion using FastAPI router
    
    