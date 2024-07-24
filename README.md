# Employee-management-application
Employee management application

## Requirement
- Login endpoint with authentication
- Employee endpoint with crud operation
	- create new employee endpoint 
	- read employee data endpoint (get all)
	- update employee endpoint 
	- delete ( terminate ) employee endpoint
- Position endpoint with crud operation 
	- create new position endpoint 
	- read position data endpoint (get all)
	- update position data endpoint 
	- delete position endpoint (with condition it should not already use)
- Department endpoint with crud operation 
	- create new department endpoint 
	- read department data endpoint (get all)
	- update department data endpoint
	- delete department endpoint (with condition it should not already use) 
- Status endpoint with crud operation
	- create new status endpoint 
	- read status data endpoint (get all) 
	- update status data endpoint 
	- delete status endpoint (with condition it should not already use)
- Advance query endpoint 
	- query with dynamic filter such as position, department and status

## Project structure guideline
```
.
├── handler                             # handler store all handler process that handle code life cycle such as api endpoint or process
│   ├── event_handler.py                # store event handler code such as dependency injection
│   ├── inputbd                         # store all input that come from client such as request body
│   │   └── input1.py                   # input body 1 for use case 1
│   ├── process or endpoint             # store endpoint or something that attach use case
│   │   ├── endpoint1.py                # endpoint 1 that attach use case 1
│   │   └── process1.py                 # process 1 that attach use case 1
│   └── run.py                          # run file for start this project
├── hexagonalmodel                      # this folder contain all core domain such as business logic, dependency, aggregate data
│   ├── adapter                         # this folder contain adapter (dependency) that use in any use case such as database, mqtt, redis
│   │   ├── production                  # this folder contain production adapter 
│   │   │   ├── prodadapter1.py         # store production adapter 1 that implement by hexagonalmodel/port/abstrac1.py
│   │   │   └── prodadapter2.py         # store production adapter 2 that implement by hexagonalmodel/port/abstrac2.py
│   │   └── test                        # this folder contain test adapter that use in unit test
│   │       ├── mockadapter1.py         # store mockadapter 1 that implement by hexagonalmodel/port/abstrac1.py
│   │       └── mockadapter2.py         # store mockadater 2 that implement by hexagonalmodel/port/abstrac2.py
│   ├── domain                          # this folder contain all core domain such as usecase (business logic)
│   │   ├── base                        # this folder contain base file 
│   │   │   ├── exception.py            # store custom execption
│   │   │   ├── logging.py              # store custom logging object
│   │   │   ├── registry.py             # store repository that call by usecase (business logic)
│   │   │   ├── singleton.py            # store singleton class (meta class of registry) that make registry are global
│   │   │   └── utils.py                # store utilize function such as pack data function
│   │   ├── model                       # contain model that use in this project such as zigbee command model or aggregate model
│   │   │   ├── model1.py               # model 1
│   │   │   └── model2.py               # model 2
│   │   └── usecase                     # this folder contain use case (business logic)
│   │       ├── usecase1.py             # business logic 1 
│   │       └── usecase2.py             # business logic 2
│   └── port                            # this folder contain abstract class of dependency that use in this project
│       ├── abstract1.py                # abstract class 1 for dependency 1
│       └── abstract2.py                # abstract class 2 for dependency 2
└── infrastructure                      # this folder contain all config file
    ├── config                          # config folder
    │   └── config.json                 # config file
    ├── database                        # database config folder
    │   └── databaseuri.py              # store database probperty such as database URI or connection code
    └── environment                     # store environment config file
    │   └── .env                        # environment file
├── test                                # this folder contain all unit test 
│   └── test_usecase1_dosomething.py    # store test case of usecase1
|   └── test_usecase2_dosomething2.py   # store test case of usecase2
```
## Code design diagram

![alt text](image.png)

## Adapter implementation guideline

![alt text](image-1.png)

## Code pattern description 

This project follow with TDD,SOLID and Hexagonal Architecture all of them enhance this project for more readable, maintainable and flexible 

## Run unit test 

```
pytest tests
```

## Coverage report 

```
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
handler/__init__.py                                  0      0   100%
handler/inputbody/__init__.py                        5      0   100%
handler/inputbody/account.py                         5      0   100%
handler/inputbody/department.py                     14      0   100%
handler/inputbody/employee.py                       29      0   100%
handler/inputbody/position.py                       16      0   100%
handler/inputbody/status.py                         11      0   100%
hexagonalmodel/adapter/test/mockdb.py               52     17    67%
hexagonalmodel/adapter/test/mockencrypt.py           4      0   100%
hexagonalmodel/adapter/test/mockstorage.py           5      1    80%
hexagonalmodel/domain/base/exception.py             24      0   100%
hexagonalmodel/domain/base/registry.py              10      0   100%
hexagonalmodel/domain/base/settings.py              11      0   100%
hexagonalmodel/domain/base/singleton.py              7      0   100%
hexagonalmodel/domain/model/__init__.py              5      0   100%
hexagonalmodel/domain/model/account.py              10      0   100%
hexagonalmodel/domain/model/department.py            7      0   100%
hexagonalmodel/domain/model/employee.py             18      0   100%
hexagonalmodel/domain/model/position.py              8      0   100%
hexagonalmodel/domain/model/status.py                6      0   100%
hexagonalmodel/domain/usecase/__init__.py            5      0   100%
hexagonalmodel/domain/usecase/account.py            16      3    81%
hexagonalmodel/domain/usecase/department.py         21      0   100%
hexagonalmodel/domain/usecase/employee.py           52      6    88%
hexagonalmodel/domain/usecase/position.py           21      0   100%
hexagonalmodel/domain/usecase/status.py             21      0   100%
hexagonalmodel/port/db.py                           52      0   100%
hexagonalmodel/port/encryption.py                    4      0   100%
hexagonalmodel/port/storage.py                       5      0   100%
tests/__init__.py                                    0      0   100%
tests/account/__init__.py                            0      0   100%
tests/account/test_login.py                         63      0   100%
tests/department/__init__.py                         0      0   100%
tests/department/test_create_new_department.py      26      0   100%
tests/department/test_delete_department.py          24      0   100%
tests/department/test_get_all_department.py         21      0   100%
tests/department/test_update_department.py          25      0   100%
tests/employee/__init__.py                           0      0   100%
tests/employee/test_create_new_employee.py         106      0   100%
tests/employee/test_get_all_employee.py             22      0   100%
tests/employee/test_get_employee_with_flter.py      16      0   100%
tests/employee/test_terminate_employee.py           21      0   100%
tests/employee/test_update_employee.py              48      0   100%
tests/position/__init__.py                           0      0   100%
tests/position/test_create_new_position.py          34      0   100%
tests/position/test_delete_position.py              33      0   100%
tests/position/test_get_all_position.py             22      0   100%
tests/position/test_update_position.py              25      0   100%
tests/status/__init__.py                             0      0   100%
tests/status/test_create_new_status.py              24      0   100%
tests/status/test_delete_status.py                  24      0   100%
tests/status/test_get_all_status.py                 22      0   100%
tests/status/test_update_status.py                  26      0   100%
--------------------------------------------------------------------
TOTAL                                             1026     27    97%
```