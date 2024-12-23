from operator import itemgetter


class Orchestra:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class MusicalComposition:
    def __init__(self, id, name, author, orchestra_id):
        self.id = id
        self.name = name
        self.author = author
        self.orchestra_id = orchestra_id


class MusicalCompositionOrchestra:
    def __init__(self, orchestra_id, composition_id):
        self.orchestra_id = orchestra_id
        self.composition_id = composition_id


orchestras = [
    Orchestra(1, "Leningrad Philharmonic"),
    Orchestra(2, "Benzogang Orchestra"),
    Orchestra(3, "Budapest Festival Orchestra"),
]

musicalCompositions = [
    MusicalComposition(1, "Morning", "Edward Grieg", 1),
    MusicalComposition(2, "Moonlight Sonata", "Ludwig van Beethoven", 2),
    MusicalComposition(3, "Saber Dance", "Aram Khachaturian", 3),
    MusicalComposition(4, "Summer Storm", "Antonio Vivaldi ", 3),
    MusicalComposition(5, "Fly", "Ludovico Einaudi", 1),
    MusicalComposition(6, "I'm swimming in the river", "Ivan Dremin", 1)
]

composition_to_orchestra = [
    MusicalCompositionOrchestra(1, 1),
    MusicalCompositionOrchestra(2, 2),
    MusicalCompositionOrchestra(3, 3),
    MusicalCompositionOrchestra(3, 4),
    MusicalCompositionOrchestra(1, 5),
    MusicalCompositionOrchestra(1, 6),

]


def first_task(composition_list):
    return sorted(composition_list, key=itemgetter(0))


def second_task(composition_list):
    res = []
    temp = dict()
    for i in composition_list:
        if i[2] in temp:
            temp[i[2]] += 1
        else:
            temp[i[2]] = 1
    for i in temp.keys():
        res.append((i, temp[i]))

    res.sort(key=itemgetter(1), reverse=True)
    return res


def third_task(composition_list, suffix):
    res = [(i[0], i[2]) for i in composition_list if str(i[1]).endswith(suffix)]
    return res


def main():
    one_to_many = [(composition.name, composition.author, orchestra.name)
                   for orchestra in orchestras
                   for composition in musicalCompositions
                   if composition.orchestra_id == orchestra.id]

    many_to_many_temp = [(orchestra.name, relation.orchestra_id, relation.composition_id)
                         for orchestra in orchestras
                         for relation in composition_to_orchestra
                         if relation.orchestra_id == orchestra.id]

    many_to_many = [(composition.name, composition.author, orchestra_name)
                    for orchestra_name, orchestra_id, composition_id in many_to_many_temp
                    for composition in musicalCompositions if composition.id == composition_id]

    print("\nSelection Б1:")
    print(first_task(one_to_many))
    print("\n")

    print("\nSelection Б2")
    print(second_task(one_to_many))
    print("\n")


    print("\nSelection Б3")
    print(third_task(many_to_many, 'n'))
    print("\n")



if __name__ == '__main__':
    main()
