def create_readme_format(model_name, benchmark_results):
    first_column_str = f"| Language Name     |"
    second_column_str = " Language Code |"
    third_column_str = f" Supported by {model_name} |"
    result_string = first_column_str + second_column_str + third_column_str + "\n"
    first_column_len = 19
    second_column_len = 15
    third_column_len = len(third_column_str) - 1

    result_string += f"|{first_column_len * '-'}|{second_column_len * '-'}|{third_column_len *'-'}|" + "\n"

    for benchmark_result in benchmark_results:
        next_row = f"| {benchmark_result['language_name']}{' ' * (first_column_len - len(benchmark_result['language_name']) - 1)}"
        next_row += f"| {benchmark_result['ISO_639_1_code']}{' ' * (second_column_len - len(benchmark_result['ISO_639_1_code']) - 1)}"
        next_row += f"| {benchmark_result['supported_language']}{' ' * (third_column_len - len(str(benchmark_result['supported_language'])) - 1)}|"
        next_row += "\n"
        result_string += next_row

    print(result_string)
    return result_string
