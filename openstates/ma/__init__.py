import datetime

metadata = {
    'lower_chamber_title': 'Representative',
    'lower_chamber_name': 'House of Representatives',
    'upper_chamber_title': 'Senator',
    'terms': [
        {
            'end_year': 2010,
            'start_year': 2009,
            'name': '186',
            'sessions': [ '186th Session (2009-2010)' ]
        },
        {
            'end_year': 2012,
            'start_year': 2011,
            'name': '187',
            'sessions': [ '187th Session(2011-2012)' ]
        }
    ],
    'name': 'Massachussetts',
    'upper_chamber_term': 2,
    'abbreviation': 'ma',
    'upper_chamber_name': 'Senate',
    'session_details': {
        '186': {
            'type': 'primary',
        },
        '187': {
            'type': 'primary',
        }
    },
    'legislature_name': 'Massachussetts General Court',
    'lower_chamber_term': 2,
    'districts': {
        # See: http://www.sec.state.ma.us/ele/ele10/state_election_cand_10.htm
        'upper': [
            "BERKSHIRE, HAMPSHIRE & FRANKLIN",
            "BRISTOL & NORFOLK",
            "FIRST BRISTOL & PLYMOUTH",
            "SECOND BRISTOL & PLYMOUTH",
            "CAPE & ISLANDS",
            "FIRST ESSEX",
            "SECOND ESSEX",
            "FIRST ESSEX & MIDDLESEX",
            "SECOND ESSEX & MIDDLESEX",
            "THIRD ESSEX & MIDDLESEX",
            "HAMPDEN",
            "FIRST HAMPDEN & HAMPSHIRE",
            "SECOND HAMPDEN & HAMPSHIRE",
            "HAMPSHIRE & FRANKLIN",
            "FIRST MIDDLESEX",
            "SECOND MIDDLESEX",
            "THIRD MIDDLESEX",
            "FOURTH MIDDLESEX",
            "MIDDLESEX & ESSEX",
            "FIRST MIDDLESEX & NORFOLK",
            "SECOND MIDDLESEX & NORFOLK",
            "MIDDLESEX, SUFFOLK & ESSEX",
            "MIDDLESEX & WORCESTER",
            "NORFOLK, BRISTOL & MIDDLESEX",
            "NORFOLK, BRISTOL & PLYMOUTH",
            "NORFOLK & PLYMOUTH",
            "PLYMOUTH & BARNSTABLE",
            "FIRST PLYMOUTH & BRISTOL",
            "SECOND PLYMOUTH & BRISTOL",
            "PLYMOUTH & NORFOLK",
            "FIRST SUFFOLK",
            "SECOND SUFFOLK",
            "FIRST SUFFOLK & MIDDLESEX",
            "SECOND SUFFOLK & MIDDLESEX",
            "SUFFOLK & NORFOLK",
            "FIRST WORCESTER",
            "SECOND WORCESTER",
            "WORCESTER, HAMPDEN, HAMPSHIRE & FRANKLIN",
            "WORCESTER & MIDDLESEX",
            "WORCESTER & NORFOLK"
        ],
        'lower': [
            "FIRST BARNSTABLE",
            "SECOND BARNSTABLE",
            "THIRD BARNSTABLE",
            "FOURTH BARNSTABLE",
            "FIFTH BARNSTABLE",
            "BARNSTABLE, DUKES & NANTUCKET",
            "FIRST BERKSHIRE",
            "SECOND BERKSHIRE",
            "THIRD BERKSHIRE",
            "FOURTH BERKSHIRE",
            "FIRST BRISTOL",
            "SECOND BRISTOL",
            "THIRD BRISTOL",
            "FOURTH BRISTOL",
            "FIFTH BRISTOL",
            "SIXTH BRISTOL",
            "SEVENTH BRISTOL",
            "EIGHTH BRISTOL",
            "NINTH BRISTOL",
            "TENTH BRISTOL",
            "ELEVENTH BRISTOL",
            "TWELFTH BRISTOL",
            "THIRTEENTH BRISTOL",
            "FOURTEENTH BRISTOL",
            "FIRST ESSEX",
            "SECOND ESSEX",
            "THIRD ESSEX",
            "FOURTH ESSEX",
            "FIFTH ESSEX",
            "SIXTH ESSEX",
            "SEVENTH ESSEX",
            "EIGHTH ESSEX",
            "NINTH ESSEX",
            "TENTH ESSEX",
            "ELEVENTH ESSEX",
            "TWELFTH ESSEX",
            "THIRTEENTH ESSEX",
            "FOURTEENTH ESSEX",
            "FIFTEENTH ESSEX",
            "SIXTEENTH ESSEX",
            "SEVENTEENTH ESSEX",
            "EIGHTEENTH ESSEX",
            "FIRST FRANKLIN",
            "SECOND FRANKLIN",
            "FIRST HAMPDEN",
            "SECOND HAMPDEN",
            "THIRD HAMPDEN",
            "FOURTH HAMPDEN",
            "FIFTH HAMPDEN",
            "SIXTH HAMPDEN",
            "SEVENTH HAMPDEN",
            "EIGHTH HAMPDEN",
            "NINTH HAMPDEN",
            "TENTH HAMPDEN",
            "ELEVENTH HAMPDEN",
            "TWELFTH HAMPDEN",
            "FIRST HAMPSHIRE",
            "SECOND HAMPSHIRE",
            "THIRD HAMPSHIRE",
            "FIRST MIDDLESEX",
            "SECOND MIDDLESEX",
            "THIRD MIDDLESEX",
            "FOURTH MIDDLESEX",
            "FIFTH MIDDLESEX",
            "SIXTH MIDDLESEX",
            "SEVENTH MIDDLESEX",
            "EIGHTH MIDDLESEX",
            "NINTH MIDDLESEX",
            "TENTH MIDDLESEX",
            "ELEVENTH MIDDLESEX",
            "TWELFTH MIDDLESEX",
            "THIRTEENTH MIDDLESEX",
            "FOURTEENTH MIDDLESEX",
            "FIFTEENTH MIDDLESEX",
            "SIXTEENTH MIDDLESEX",
            "SEVENTEENTH MIDDLESEX",
            "EIGHTEENTH MIDDLESEX",
            "NINETEENTH MIDDLESEX",
            "TWENTIETH MIDDLESEX",
            "TWENTY-FIRST MIDDLESEX",
            "TWENTY-SECOND MIDDLESEX",
            "TWENTY-THIRD MIDDLESEX",
            "TWENTY-FOURTH MIDDLESEX",
            "TWENTY-FIFTH MIDDLESEX",
            "TWENTY-SIXTH MIDDLESEX",
            "TWENTY-SEVENTH MIDDLESEX",
            "TWENTY-EIGHTH MIDDLESEX",
            "TWENTY-NINTH MIDDLESEX",
            "THIRTIETH MIDDLESEX",
            "THIRTY-FIRST MIDDLESEX",
            "THIRTY-SECOND MIDDLESEX",
            "THIRTY-THIRD MIDDLESEX",
            "THIRTY-FOURTH MIDDLESEX",
            "THIRTY-FIFTH MIDDLESEX",
            "THIRTY-SIXTH MIDDLESEX",
            "THIRTY-SEVENTH MIDDLESEX",
            "FIRST NORFOLK",
            "SECOND NORFOLK",
            "THIRD NORFOLK",
            "FOURTH NORFOLK",
            "FIFTH NORFOLK",
            "SIXTH NORFOLK",
            "SEVENTH NORFOLK",
            "EIGHTH NORFOLK",
            "NINTH NORFOLK",
            "TENTH NORFOLK",
            "ELEVENTH NORFOLK",
            "TWELFTH NORFOLK",
            "THIRTEENTH NORFOLK",
            "FOURTEENTH NORFOLK",
            "FIFTEENTH NORFOLK",
            "FIRST PLYMOUTH",
            "SECOND PLYMOUTH",
            "THIRD PLYMOUTH",
            "FOURTH PLYMOUTH",
            "FIFTH PLYMOUTH",
            "SIXTH PLYMOUTH",
            "SEVENTH PLYMOUTH",
            "EIGHTH PLYMOUTH",
            "NINTH PLYMOUTH",
            "TENTH PLYMOUTH",
            "ELEVENTH PLYMOUTH",
            "TWELFTH PLYMOUTH",
            "FIRST SUFFOLK",
            "SECOND SUFFOLK",
            "THIRD SUFFOLK",
            "FOURTH SUFFOLK",
            "FIFTH SUFFOLK",
            "SIXTH SUFFOLK",
            "SEVENTH SUFFOLK",
            "EIGHTH SUFFOLK",
            "NINTH SUFFOLK",
            "TENTH SUFFOLK",
            "ELEVENTH SUFFOLK",
            "TWELFTH SUFFOLK",
            "THIRTEENTH SUFFOLK",
            "FOURTEENTH SUFFOLK",
            "FIFTEENTH SUFFOLK",
            "SIXTEENTH SUFFOLK",
            "SEVENTEENTH SUFFOLK",
            "EIGHTEENTH SUFFOLK",
            "NINETEENTH SUFFOLK",
            "FIRST WORCESTER",
            "SECOND WORCESTER",
            "THIRD WORCESTER",
            "FOURTH WORCESTER",
            "FIFTH WORCESTER",
            "SIXTH WORCESTER",
            "SEVENTH WORCESTER",
            "EIGHTH WORCESTER",
            "NINTH WORCESTER",
            "TENTH WORCESTER",
            "ELEVENTH WORCESTER",
            "TWELFTH WORCESTER",
            "THIRTEENTH WORCESTER",
            "FOURTEENTH WORCESTER",
            "FIFTEENTH WORCESTER",
            "SIXTEENTH WORCESTER",
            "SEVENTEENTH WORCESTER",
            "EIGHTEENTH WORCESTER"
        ]
    }
}
