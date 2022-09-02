from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Material(Base):
    __tablename__ = 'materials'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    authors = Column(String, nullable=False)
    edition = Column(Integer, nullable=True)

    def __repr__(self):
        return "<Material(name='{}', authors='{}', edition='{}')>" \
            .format(self.name, self.authors, self.edition)


class LinkWithTerm(Base):
    __tablename__ = 'links_with_term'
    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey(Material.id), nullable=False)
    ontology_term = Column(String, nullable=False)
    material_term = Column(String, nullable=False)
    page = Column(Integer, nullable=False)
    number_on_page = Column(Integer, nullable=False)
    topic = Column(String, nullable=False)

    def __repr__(self):
        return "<link_with_term(material_id='{}', ontology_term='{}', material_term='{}', " \
               "page='{}', number_on_page='{}', topic='{}')>"\
            .format(self.material_id, self.ontology_term, self.material_term,
                    self.page, self.number_on_page, self.topic)


class LinkWithTask(Base):
    __tablename__ = 'links_with_task'
    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey(Material.id), nullable=False)
    ontology_term = Column(String, nullable=False)
    page = Column(Integer, nullable=False)
    task_number = Column(String, nullable=False)
    topic = Column(String, nullable=False)

    def __repr__(self):
        return "<link_with_task(material_id='{}', ontology_term='{}', page='{}', task_number='{}', topic='{}')>" \
            .format(self.material_id, self.ontology_term, self.page, self.task_number, self.topic)


class LinkWithTopic(Base):
    __tablename__ = 'links_with_topic'
    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey(Material.id), nullable=False)
    ontology_term = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    start_page = Column(Integer, nullable=False)
    end_page = Column(Integer, nullable=False)

    def __repr__(self):
        return "<link_with_task(material_id='{}', ontology_term='{}', topic='{}', start_page='{}', end_page='{}')>"\
            .format(self.material_id, self.ontology_term, self.topic, self.start_page, self.end_page)
