def lambda_handler(event, context):
    args = None
    if 'args' in event:
        args = event['args']

    return {
        'message': 'Hello world! Your submitted arguments: {}!'.format(args)
    }
