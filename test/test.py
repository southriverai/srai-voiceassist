from srai_voiceassist.client_openai_audio import ClientOpenaiAudio
from srai_voiceassist.service_playback import ServicePlayback
from srai_voiceassist.service_prompt import ServicePrompt
from srai_voiceassist.service_record import ServiceRecord
from srai_voiceassist.service_transcribe import ServiceTranscribe


def test_forward():
    service_record = ServiceRecord()
    service_transcribe = ServiceTranscribe()
    service_prompt = ServicePrompt()
    # service_playback = ServicePlayback()
    client_openai_audio = ClientOpenaiAudio()

    try:
        while True:
            # service_playback.start()

            audio = service_record.record_audio()
            text = service_transcribe.transcribe_audio(audio)
            # with open("1721629556.wav", "rb") as file:
            #     audio_bytes = file.read()
            # text = service_transcribe.transcribe_for_file("1721629556.wav")
            print("!!!!!")
            print(text)
            print("!!!!!")
            response = service_prompt.prompt_with_perplexity(text)
            print("#####")
            print(response)
            print("#####")
            client_openai_audio.play(response)

    except Exception as e:
        # service_playback.join()
        raise e


def test_playback():
    service_playback = ServicePlayback("wav")
    service_playback.start()
    with open("response.opus", "rb") as file:
        service_playback.enqueue_bytes(file.read())
    service_playback.join()


if __name__ == "__main__":
    test_forward()
    # test_playback()
