from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API Key here
openai.api_key = 'your_openai_api_key'

@app.route('/generate_logo', methods=['POST'])
def generate_logo():
    data = request.get_json()
    description = data.get('description', '')

    if not description:
        return jsonify({'success': False, 'message': 'No description provided'}), 400

    try:
        # Use OpenAI's DALL-E or another model to generate the logo
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="512x512",  # Can adjust the size here
            response_format="url"
        )

        logo_url = response['data'][0]['url']
        return jsonify({'success': True, 'logo_url': logo_url})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)