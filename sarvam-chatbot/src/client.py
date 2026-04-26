import os
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()


class _LazySarvamClient:
	"""Create the SDK client only when it is first used."""

	def __init__(self) -> None:
		self._client = None

	def _get_client(self) -> SarvamAI:
		if self._client is None:
			api_key = os.getenv("SARVAM_API_KEY")
			if not api_key:
				raise RuntimeError(
					"SARVAM_API_KEY is missing. Add it to your environment or .env file."
				)
			self._client = SarvamAI(api_subscription_key=api_key)
		return self._client

	def __getattr__(self, item):
		return getattr(self._get_client(), item)


client = _LazySarvamClient()