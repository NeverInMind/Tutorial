import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    new_arr = []
    for item in cats:
        if isinstance(item, Cat):
            res = {
                'nickname': item.nickname,
                'age': item.age,
                'owner': item.owner
            }
            new_arr.append(res)
        elif isinstance(item, dict):
            my_timple = Cat(**item)
            new_arr.append(my_timple)
        else:
            return cats
    return new_arr