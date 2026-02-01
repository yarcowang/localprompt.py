import requests


class LocalPrompt:
    """A Python client library for Prompt Studio API."""

    def __init__(self, base_url: str):
        """Initialize the LocalPrompt client.

        Args:
            base_url: The base URL of the Prompt Studio server.
                      Example: "http://localhost:30017"
        """
        self.base_url = base_url.rstrip('/')

    def _get(self, endpoint: str) -> dict | None:
        """Make a GET request to the API.

        Args:
            endpoint: The API endpoint path.

        Returns:
            The response data dict, or None if the request failed.
        """
        url = f'{self.base_url}{endpoint}'
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get('success') and data.get('data'):
                return data['data']
            return None
        except requests.RequestException:
            return None

    def get_prompt_by_id(self, prompt_id: int) -> dict | None:
        """Get a prompt by its ID.

        Args:
            prompt_id: The prompt ID.

        Returns:
            A dict containing the prompt data, or None if not found.
        """
        return self._get(f'/prompts/{prompt_id}')

    def get_prompt_by_slug(self, prompt_slug: str) -> dict | None:
        """Get a prompt by its slug.

        Args:
            prompt_slug: The prompt slug.

        Returns:
            A dict containing the prompt data, or None if not found.
        """
        return self._get(f'/prompts/slug/{prompt_slug}')

    def get_prompt(self, prompt_id_or_slug: int | str) -> dict | None:
        """Get a prompt by ID or slug.

        Args:
            prompt_id_or_slug: The prompt ID (int) or slug (str).

        Returns:
            A dict containing the prompt data, or None if not found.
        """
        if isinstance(prompt_id_or_slug, int):
            return self.get_prompt_by_id(prompt_id_or_slug)
        return self.get_prompt_by_slug(prompt_id_or_slug)
