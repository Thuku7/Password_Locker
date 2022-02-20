class Credentials:
    '''
    class that generates an instance of credential 
    '''

    credential_requirements = []

    def __init__(self, social_name, social_user_name, social_user_password):

        self.social_name = social_name
        self.social_user_name = social_user_name
        self.social_user_password = social_user_password


    def save_credentials(self):
        '''
        Method that saves a credential object in the credential_requirements array
        '''

        Credentials.credential_requirements.append(self)

    def delete_credentials(self):
        '''
        Function that will delete a users credential
        '''

        Credentials.credential_requirements.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        returns the credential list
        '''

        return cls.credential_requirements

    @classmethod
    def find_credentials(cls,social):
        '''
        Function that will take in a platform name and return the credentials that match
        Args:
            platform_name: name of the credential to search for
        Return:
            Credentials that match the platform_name
        '''

        for credential in cls.credential_requirements:
            if credential.social_name == social:
                return credential
        
    @classmethod
    def credential_exists(cls, social):
        '''
        Function that will check for a credential exists from the credential list
        Args:
            Social: name to search if the credential exists
        Returns:
            Boolea: True or False
            
        '''

        for credential in cls.credential_requirements:
            if credential.social_name == social:
                return True

        return False
