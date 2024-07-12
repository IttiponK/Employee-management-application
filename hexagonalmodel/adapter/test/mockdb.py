from hexagonalmodel.domain.model.account import AccountModel
from hexagonalmodel.port.db import DbPort 

class MockDb(DbPort):
    
    def get_account_detail_by_username(self, username: str) -> AccountModel:
        pass 
    