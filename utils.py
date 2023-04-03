def make_query_response(cmd, val, file_or_result):
    match cmd:
        case "filter":
            return list(filter(lambda x: val in x, file_or_result))
        case "map":
            return '\n'.join([x.split()[int(val)] for x in file_or_result])
        case "unique":
            return list(set(file_or_result))
        case "sort":
            return sorted(file_or_result, reverse=val == 'desc')
        case "limit":
            return list(file_or_result)[:int(val)]
