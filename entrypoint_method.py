import argparse
import os
import requests
import subprocess

def run_method(output_dir, name, bam_input, ref_input, parameters):
    """
    So rmarkdown::render is called pointing to a Rmd script placed within (sys.path[0]) this very script dir
    Caution the rmarkdown output directory specification is confusing: '.' propagates the 'out/{name}' path
    """
    subprocess.run(
        ["Rscript", "-e", "rmarkdown::render('%s', \
                  param=list(input_files_mapping='%s', \
                             outputs_directory='%s'), \
                  output_file = '%s', \
                  output_dir = '%s')" %(op.join(sys.path[0], '04_metric_collector.Rmd'),
                                         op.abspath(metrics_metafile),
                                         op.abspath(op.join(output_dir, '..')),
                                         report_basename,
                                         op.abspath(output_dir)) ],
        cwd = output_dir,
    )

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Run method on files.')

    # Add arguments
    parser.add_argument('--output_dir', type=str, help='output directory where metric repot will be saved.')
    parser.add_argument('--metric.scores', type=str, nargs='+', help='Metrics files.')

    # Parse arguments
    args, extra_arguments = parser.parse_known_args()

    content = " ".join(extra_arguments)
    with open("/home/projects/dtu_00062/people/sorsan/ob_anonymization_dataloss/test.txt", 'w') as file:
        file.write(content)
    

    output_dir = getattr(args, 'output_dir')
    files = getattr(args, 'metric.scores')

    files = [op.abspath(x) for x in files]
    with open(op.join(output_dir, 'inputs.txt'), 'w') as fh:
        fh.write("\n".join(map(str, files)))

#    run_method(output_dir = output_dir,
#               metrics_metafile = op.join(output_dir, 'inputs.txt'),
#               report_basename = 'plotting_report.html')

if __name__ == "__main__":
    main()
