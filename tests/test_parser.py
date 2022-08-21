from fractions import Fraction
from decimal import Decimal

from chchart_parser.chart import Chart
from chchart_parser.enums import EPlayer2, EEventType


def test_parse_metadata(chart: Chart):
    assert chart.metadata is not None, 'metadata is none'
    assert chart.metadata.name == 'Victory'
    assert chart.metadata.artist == 'Andy James'
    assert chart.metadata.charter == 'GuitarZero132'
    assert chart.metadata.album == 'Exodus'
    assert chart.metadata.year == 2017
    assert chart.metadata.offset == 0
    assert chart.metadata.resolution == 192
    assert chart.metadata.player2 == EPlayer2.bass
    assert chart.metadata.difficulty == 0
    assert chart.metadata.preview_start == 0
    assert chart.metadata.preview_end == 0
    assert chart.metadata.genre == 'rock'
    assert chart.metadata.media_type == 'cd'
    assert chart.metadata.music_stream == 'song.ogg'


def test_parse_events(chart: Chart):
    ticks = [
        1536, 7680, 13824, 19968, 27648, 33792, 39936,
        46080, 52224, 59904, 66048, 72192, 78336, 84480,
        90624, 93696, 99840, 105984, 112128, 118272,
        124416, 130560, 135168, 141312,
    ]
    texts = [
        'Main Riff 1A', 'Main Riff 1B', 'Verse 1A',
        'Verse 1B', 'Chorus 1A', 'Chorus 1B',
        'Main Riff 2', 'Verse 2A', 'Verse 2B',
        'Chorus 2A', 'Chorus 2B', 'Guitar Solo 1A',
        'Guitar Solo 1B', 'Guitar Solo 1C', 'Guitar Solo 1D',
        'Main Riff 3', 'Bridge A', 'Bridge B',
        'Guitar Solo 2A', 'Guitar Solo 2B', 'Guitar Solo 2C',
        'Guitar Solo 2D', 'Chorus 3A', 'Chorus 3B', 'Outro',
    ]

    for tick, text, event in zip(ticks, texts, chart.events):
        assert event.tick == tick
        assert event.type == EEventType.SECTION
        assert event.text == text


def test_parse_sync(chart: Chart):
    expecteds = [
        {
            'tick': 0,
            'time_signature': Fraction(4, 16),
            'bpm': Decimal(169.0)
        },
        {
            'tick': 1536,
            'time_signature': Fraction(4, 16),
            'bpm': Decimal(165.0)
        }
    ]
    assert len(chart.sync) == len(expecteds)

    for actual, expected in zip(chart.sync, expecteds):
        assert actual.tick == expected['tick']
        assert actual.time_signature == expected['time_signature']
        assert actual.bpm == expected['bpm']


def test_parse_note_charts(chart: Chart):
    assert len(chart.charts.ExpertSingle) == 1521
