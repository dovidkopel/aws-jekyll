import boto3

def lambda_handler(event, context):
    sess = boto3.client('codebuild')
    
    for r in event['Records']:
        _envs = []
        commit_data = r['codecommit']
        refs = commit_data['references']
        
        if refs and len(refs) == 1:
            ref_data = refs[0]
            ref = ref_data['ref']
            commit = ref_data['commit']
            print(ref, commit)
            
            if 'staging' in ref:
                print('staging')
                _envs.append({
                    'name': 'BUCKET',
                    'value': 'staging.dovidkopel.com',
                    'type': 'PLAINTEXT'
                })
            else:
                print('master')

            sess.start_build(
                projectName='dovidkopel-blog',
                sourceVersion=commit,
                environmentVariablesOverride=_envs
            )
