from gendiff.formatters import json, string, plain

available_formatters = {
    'json': json.render,
    'plain': plain.render,
    'string': string.render,
}