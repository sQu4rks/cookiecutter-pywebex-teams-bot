FUNC_TPL="""
@app.route('/webhook/{resource}/{event}', methods=['POST'])
def webhook_{resource}_{event}():
    raw_json = request.get_json()

"""

def create_func(resource, event):
   tmp =  FUNC_TPL.format(resource=resource, event=event)
   tmp += "    return jsonify({'success': True})\n"

   return tmp

import yaml

f = yaml.safe_load(open("vars.yml"))

for resource, events in f['webhooks'].items():
    for e in events: 
        print(create_func(resource, e))
