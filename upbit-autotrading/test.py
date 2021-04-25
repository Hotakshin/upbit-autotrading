import pyupbit

access = "eCZGW6UBUfGEgrv5Au7Y7OWFuP61FvtyZ7zbx0NF"          # 본인 값으로 변경
secret = "RXTgeFQyCRDu2x0OomOTYiQGuEWxf01gV25ucmPf"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회