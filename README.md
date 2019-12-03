This is the API implementation of the [Deezer](https://www.deezer.com) Spleeter project : [https://github.com/deezer/spleeter](https://github.com/deezer/spleeter)

</br>
Spleeter API will separate the input audio source into multiple audio files with their associated stems described as follow :

* Vocals (singing voice) / accompaniment separation ([2 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-2stems-model))
* Vocals / drums / bass / other separation ([4 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-4stems-model))
* Vocals / drums / bass / piano / other separation ([5 stems](https://github.com/deezer/spleeter/wiki/2.-Getting-started#using-5stems-model))

</br>

[Spleeter: A Fast And State-of-the Art Music Source Separation Tool With Pre-trained Models](http://archives.ismir.net/ismir2019/latebreaking/000036.pdf)
```
 @misc{spleeter2019,
  title={Spleeter: A Fast And State-of-the Art Music Source Separation Tool With Pre-trained Models},
  author={Romain Hennequin and Anis Khlif and Felix Voituret and Manuel Moussallam},
  howpublished={Late-Breaking/Demo ISMIR 2019},
  month={November},
  note={Deezer Research},
  year={2019}
}
```
- - -
EXAMPLE

Audio Source Input
<audio controls="controls">
  <source type="audio/mp3" src="http://pretrained-models.auth-18b62333a540498882ff446ab602528b.storage.gra5.cloud.ovh.net/sound/spleeter/audio_example.mp3"></source>
</audio>


Vocals Output
<audio controls="controls">
  <source type="audio/wav" src="http://pretrained-models.auth-18b62333a540498882ff446ab602528b.storage.gra5.cloud.ovh.net/sound/spleeter/vocals.wav"></source></source>
</audio>

Piano Output
<audio controls="controls">
  <source type="audio/wav" src="http://pretrained-models.auth-18b62333a540498882ff446ab602528b.storage.gra5.cloud.ovh.net/sound/spleeter/piano.wav"></source></source>
</audio>

Bass Output
<audio controls="controls">
  <source type="audio/wav" src="http://pretrained-models.auth-18b62333a540498882ff446ab602528b.storage.gra5.cloud.ovh.net/sound/spleeter/bass.wav"></source></source>
</audio>

Drums Output
<audio controls="controls">
  <source type="audio/wav" src="http://pretrained-models.auth-18b62333a540498882ff446ab602528b.storage.gra5.cloud.ovh.net/sound/spleeter/drums.wav"></source></source>
</audio>

Other Output
<audio controls="controls">
  <source type="audio/wav" src="http://pretrained-models.auth-18b62333a540498882ff446ab602528b.storage.gra5.cloud.ovh.net/sound/spleeter/other.wav"></source></source>
</audio>


- - -
INPUT

```json
{
  "text": "https://github.com/deezer/spleeter/raw/master/audio_example.mp3",
  "nb_stems": 5
}
```
- - -
EXECUTION
```bash
curl -X POST "https://api-market-place.ai.ovh.net/sound-spleeter/process" -H "accept: application/zip" -H "X-OVH-Api-Key: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" -H "Content-Type: application/json" -d '{"url": "https://github.com/deezer/spleeter/raw/master/audio_example.mp3", "nb_stems": 5}' -o splitted_output.zip
```
- - -

OUTPUT
Zip file containing splitted tracks

- - -


please refer to swagger documentation for further technical details: [swagger documentation](https://market-place.ai.ovh.net/#!/apis/2d428114-d801-4bb1-8281-14d8018bb186/pages/8b94834c-43ab-4baf-9483-4c43ab7baf80)

* * *
<div>Icons made by <a href="https://www.flaticon.com/authors/kiranshastry" title="Kiranshastry">Kiranshastry</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

</br>
<div>
<small>
This documentation includes a demo audio file audio_example.mp3 which is an excerpt from Slow Motion Dream by Steven M Bryant (c) copyright 2011 Licensed under a Creative Commons Attribution (3.0) license. <a href="http://dig.ccmixter.org/files/stevieb357/34740">http://dig.ccmixter.org/files/stevieb357/34740</a> Ft: CSoul,Alex Beroza & Robert Siekawitch
</small>
</div>
