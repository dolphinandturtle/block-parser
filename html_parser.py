import os


def make_blocks(
        source, start, end,
        ignore=[],
        keep_inter=True, keep_blocks=True
):

    output = []
    i, _i, __i, temp = 0, 1, 1, ""
    while True:
        scope = source[i:_i]
        scope_tail = source[i]
        scope_range = len(scope)
        ignore_scope = [ig[0:scope_range] for ig in ignore]
        start_range = len(start)
        end_range = len(end)
        start_range = len(start)
        end_range = len(end)
        ignore_range = max([len(ig) for ig in ignore])

        if scope in ignore_scope:
            __i = _i
            while True:
                temp_scope = source[i:__i]
                temp_range = len(temp_scope)
                if temp_scope in ignore:
                    temp += temp_scope
                    i = __i
                    _i = __i
                    scope = source[i:_i]
                if temp_range > ignore_range:
                    break
                __i += 1
        if scope == start and scope:
            if keep_inter:
                output.append(temp)
            i = _i
            _i += 1
            temp = ""
        if scope == end and scope:
            if keep_blocks:
                output.append(temp)
            i = _i
            _i += 1
            temp = ""
        if scope not in [start, end]:
            _i += 1
        if scope_range > max([start_range, end_range]):
            temp += scope_tail
            i += 1
            _i = i + 1
        if i == len(source) or _i == len(source):
            break
    return output


def clean_blocks(source):
    return [_ for _ in source if _]
