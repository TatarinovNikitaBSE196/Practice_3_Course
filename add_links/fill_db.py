from database.models import Material, LinkWithTerm, LinkWithTask, LinkWithTopic
from database.db import Database

# TODO: correct pages
if __name__ == '__main__':
    print('Drop tables? [n]/y')
    drop = input()
    if drop == 'y':
        Database.init(drop_all=True)
    else:
        Database.init(drop_all=False)
    s = Database.get_session()
    if s is not None:
        s.add(Material(name='Physics. Principles with application',
                       authors='Douglas C. Giancoli',
                       edition=7))
        s.commit()
        s.add(LinkWithTerm(material_id=1,
                           ontology_term='kg*m/s',
                           material_term='momentum',
                           page=192,
                           number_on_page=2,
                           topic='Linear Momentum'))
        s.commit()
        s.add(LinkWithTask(material_id=1,
                           ontology_term='kg*m/s',
                           page=211,
                           task_number='17',
                           topic='Linear Momentum'))
        s.commit()
        s.add(LinkWithTopic(material_id=1,
                            ontology_term='kg*m/s',
                            topic='Linear Momentum',
                            start_page=191,
                            end_page=218))
        s.commit()
        s.close()
