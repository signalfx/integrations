# metric_md_generator
#
# Description: quick script to generate markdown files for individual metrics
# for intregrations docs given a YAML file describing the metrics

import yaml
import io
import sys


def generate(input_file, output_file_dir):
    with io.open(input_file, "r") as stream:
        try:
            for metrics in yaml.load_all(stream):
                for metric in metrics:
                    write_md_file(metric, output_file_dir)

        except yaml.YAMLError as exc:
            print(exc)


def write_md_file(metric, output_file_dir):
    file_path = output_file_dir + '/' + metric['type'] + '.' + \
        metric['title'].replace(' ', '_').lower() + '.md'
    f = open(file_path, 'w')
    f.write('---\n')
    f.write('title: ' + metric['title'] + '\n')
    f.write('brief: ' + (metric.get('brief', '').strip() or metric['description']) + '\n')
    f.write('metric_type: ' + metric['type'] + '\n')
    f.write('---\n')
    f.write('### ' + metric['title'] + '\n\n')
    f.write(metric['description'])
    f.close()


generate(sys.argv[1], sys.argv[2])
