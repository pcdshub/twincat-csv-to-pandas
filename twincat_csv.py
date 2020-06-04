import io
import datetime
import sys

import pandas as pd


TIME_FMT = '%A, %B %d, %Y %H:%M:%S.%f'


def berkoff_time_to_datetime(time_str):
    return datetime.datetime.strptime(time_str, TIME_FMT)


def read_beckhoff_csv(fn):
    with open(fn, 'rt') as f:
        lines = f.read().splitlines()

    start_time = berkoff_time_to_datetime(' '.join(lines[2].split('\t')[2:]))
    end_time = berkoff_time_to_datetime(' '.join(lines[3].split('\t')[2:]))
    elapsed_time = (end_time - start_time).total_seconds()

    def get_line(idx, line):
        timestamp = (start_time + idx * sample_time).isoformat()
        line = [timestamp] + line.split('\t')[1::2]
        return '\t'.join(line)

    sample_time = datetime.timedelta(seconds=elapsed_time / (len(lines) - 26))
    data = [get_line(idx, line) for idx, line in enumerate(lines[25:-1])]

    print('row count', len(data))
    print('elapsed time', elapsed_time)
    print('sample time', sample_time)
    print('start time', start_time)
    print('end time', end_time)

    metadata = lines[6:24]
    header = list(lines[6].split('\t')[1::2])

    info = {col: {} for col in header}
    for md in metadata:
        md_name = md.split('\t')[0]
        for col, md_value in zip(header, md.split('\t')[1::2]):
            info[col][md_name] = md_value

    for idx, old_name in enumerate(list(header)):
        rename = info[old_name].get('SymbolName')
        if rename:
            header[idx] = rename
            info[rename] = info.pop(old_name)

    with io.StringIO() as f:
        print('Time\t' + '\t'.join(header), file=f)
        print('\n'.join(data), file=f)
        f.seek(0)
        df = pd.read_csv(f, delimiter='\t', decimal=',')

    return info, df.set_index('Time')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        metadata, df = read_beckhoff_csv(sys.argv[1])
