import boto3
import os

def synthesize_speech(text, output_file, voice_id='Joanna', output_format='mp3'):
    """
    Synthesizes speech using Amazon Polly API and saves the result as a WAV file.
    
    Args:
        text (str): The text to be synthesized.
        output_file (str): The name of the output WAV file.
        voice_id (str): The ID of the voice to be used (e.g., 'Joanna', 'Matthew', etc.).
        output_format (str): The output format (e.g., 'mp3', 'ogg_vorbis', 'pcm').
    """
    # Initialize the Amazon Polly client
    polly_client = boto3.client(
    'polly',
    region_name='us-east-1',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)


    
    # Synthesize speech
    response = polly_client.synthesize_speech(
        Text=text,
        VoiceId=voice_id,
        OutputFormat=output_format
    )
    
    # Save the audio stream to a file
    with open(output_file, 'wb') as f:
        f.write(response['AudioStream'].read())

def main():
    text = "Hello, this is a sample text to be synthesized by Amazon Polly."
    output_file = "output.wav"  # Change this to the desired output file name
    
    synthesize_speech(text, output_file, output_format='pcm')
    print(f"Speech synthesized and saved as {output_file}")

if __name__ == "__main__":
    main()
