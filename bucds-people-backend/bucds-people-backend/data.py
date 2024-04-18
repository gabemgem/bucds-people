from .db import get_db
import click
import json


def dbRowToJson(row):
    person = {}
    for prop in row.keys():
        person[prop] = row[prop]
    return person

def fixPropNamesDbToClient(person):

    if 'researchtags' in person:
        person['researchtags'] = person['researchtags'].split(',')
    if 'affiliations' in person:
        person['affiliations'] = person['affiliations'].split(',')
    if 'othertags' in person:
        person['othertags'] = person['othertags'].split(',')


    propCorrections = {
        'name': 'Name',
        'email': 'Email',
        'type': 'Type',
        'pronouns': 'Pronouns',
        'cohort': 'Cohort',
        'researchtags': 'Research Tags',
        'researchoverview': 'Research Overview',
        'affiliations': 'Affiliations',
        'othertags': 'Other Tags'
    }

    return {propCorrections[old_key]: value for old_key, value in person.items() if old_key in propCorrections}

def fixPropNamesClientToDb(clientperson):

    propCorrections = {
        'Name': 'name',
        'Email': 'email',
        'Type': 'type',
        'Pronouns': 'pronouns',
        'Cohort': 'cohort',
        'Research Tags': 'researchtags',
        'Research Overview': 'researchoverview',
        'Affiliations': 'affiliations',
        'Other Tags': 'othertags'
    }

    person = {propCorrections[old_key]: value for old_key, value in clientperson.items() if old_key in propCorrections}

    if 'researchtags' in person:
        person['researchtags'] = person['researchtags'].split(',')
    if 'affiliations' in person:
        person['affiliations'] = person['affiliations'].split(',')
    if 'othertags' in person:
        person['othertags'] = person['othertags'].split(',')

    return person




def dbToJson():
    db = get_db()
    dbpeople = db.execute(
        'SELECT * FROM person'
    ).fetchall()

    relationships = db.execute('SELECT * FROM relationship').fetchall()

    people = {}

    for person in dbpeople:
        people[person['name']] = fixPropNamesDbToClient(dbRowToJson(person))

    for r in relationships:
        if 'Relationships' not in people[r['source']]:
            people[r['source']]['Relationships'] = []
        people[r['source']]['Relationships'].append(
            { 'name': r['target'], 'type': r['type'] } if r['type'] else 
            { 'name': r['target'] }
            )

    return people

def addTestToDB():
    error = None
    db = get_db()
    try:
        db.execute(
            'INSERT INTO person (name, email, type, pronouns, cohort, researchtags, researchoverview, affiliations, othertags)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            ('gabe', 'gabe@gabe.me', 'phd', 'He/Him', 2022, 'adb,sdm', 'overview text', 'cds,cmac', 'tag')
        )
        db.execute(
            'INSERT INTO person (name, email, type, pronouns, cohort, researchtags, researchoverview, affiliations, othertags)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            ('gabe2', 'gabe@gabe.me', 'phd', 'He/Him', 2022, 'adb,sdm', 'overview text', 'cds,cmac', 'tag')
        )
        db.execute(
            'INSERT INTO relationship (source, target, type)'
            ' VALUES (?, ?, ?)',
            ('gabe', 'gabe2', 'buds')
        )
        db.execute(
            'INSERT INTO relationship (source, target)'
            ' VALUES (?, ?)',
            ('gabe2', 'gabe')
        )
        db.commit()
    except db.IntegrityError:
        error = 'integrity error'

    if error is not None:
        print(error)


@click.command('testdata')
def testdata():
    addTestToDB()
    output = dbToJson()
    pretty_json = json.dumps(output, indent=4)
    print(pretty_json)

def init_app(app):
    app.cli.add_command(testdata)