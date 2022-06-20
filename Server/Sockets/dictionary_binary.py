import pickle



def dict_to_binary(the_dict):

    return pickle.dumps(the_dict)


def binary_to_dict(the_binary):
    # try:
    return pickle.loads(the_binary)
    # except:
    #     print("Data ran out of input ")
