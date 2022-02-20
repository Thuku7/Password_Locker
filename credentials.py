class Credentials:
    """
    class that generates an instance of credentials
    """

    credential_requirments = []


    def __init__(self,social_name,social_user_name,social_user_password):

        self.social_name = social_name
        self.social_user_name = social_user_name
        self.social_user_password = social_user_password


    def save_credentials(self):
        """
        Method that saves credential object in the credential_requirements array

        """

        Credentials.credential_requirements.append(self)

    def delete_credentials(self):
        """
        Function that will delete a users credential
        """ 

        Credentials.credential_requirements.remove(self)   


    @classmethod
    def dispaly_credentials(cls):
        """
        returns the credential list
        """ 

        return cls.credential_requirements       