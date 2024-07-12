from abc import ABC,abstractmethod
from hexagonalmodel.domain.model.account import AccountModel

class DbPort(ABC):
    
    @abstractmethod
    def get_account_detail_by_username(self,username: str) -> AccountModel:
        """ get account detail data that match with username

        Args:
            username (str): user name

        Returns:
            AccountModel: model for describe this account
        """   