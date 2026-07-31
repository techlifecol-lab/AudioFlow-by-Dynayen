"""Config flow for AudioFlow."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN


class AudioFlowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):

        errors = {}

        if user_input is not None:

            return self.async_create_entry(
                title=user_input["host"],
                data=user_input,
            )

        data_schema = vol.Schema(
            {
                vol.Required("host"): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )
