# from collections.abc import Iterable	
# # from collectios will stop working	
# print(isinstance([],Iterable))	
# print(isinstance({},Iterable))	
# print(isinstance('',Iterable))	
# print(isinstance((x for x in range(10)),Iterable))	
# print(isinstance(100,Iterable))	

# from collections.abc import Iterator	
# from collectios will stop working	
# print(isinstance(iter([]),Iterator))	
# print(isinstance(iter({}),Iterator))	
# print(isinstance(iter(''),Iterator))	
# print(isinstance((x for x in range(10)),Iterator))	
# print(isinstance(100,Iterator))	

# for x in [1,2,3,4,5,6,7]:	
#     pass	

# it = iter([1,2,3,4,5,6,7])	
# while True:	
#     try:	
#         x = next(it)	
#         print(x)	
#     except StopIteration:	
#         print('StopIteration')	
#         break