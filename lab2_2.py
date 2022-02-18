import json
import twitter1
import twitter3

# data = twitter1.data_from_twitter1()
# data = twitter3.data_from_twitter3()

def analyzing_data(data):
    '''
    analyses the data and helps to navigate over nested dictionary(twitter info)
    '''
    while check_the_dict_or_the_list(data):
        if check_the_dict_or_the_list(data) == 'dict':
            print(f"You're in dictionary, choose one of the keys,for example: id or entities...")
            print('Or use exit for finishing a program')
            for key in list(data.keys()):
                print(key)
            user_choice = input('Key: ')
            if user_choice != 'exit':
                print()
                try:
                    data = data[user_choice]
                except KeyError:
                    continue
            else:
                break
        elif check_the_dict_or_the_list(data) == 'list':
            print(f"You're in list, choose one of the indices(for example: 0,1)")
            print('Or use exit for finishing a program')
            for count, val in enumerate(data):
                print(str(count) + ' : ' + str(val)[:40] + '...')
            user_choice = input('Index: ')
            if user_choice != 'exit':
                print()
                try:
                    user_choice = int(user_choice)
                except ValueError:
                    print('Invalid input, try again')
                    continue
                try:
                    data = data[user_choice]  
                except IndexError:
                    print("Invalid input, try again")
                    continue    
            else:
                break
    print('Hooray!!! You reached your final destination =)')


def check_the_dict_or_the_list(object):
    '''
    return whether the type of object is list of dict or something else
    '''
    if type(object) == list and object:
        return 'list'
    elif type(object) == dict:
        return 'dict'
    else:
        return False
analyzing_data(data)
 
