import discord


async def check_admin(interaction: discord.Interaction) -> bool:
    """
    Check if the author of the command as administrator permissions in the guild,
    and sends an ephemeral message if they don't.

    :param interaction: The current :class:`discord.Interaction`
    :return: If the author has admin
    """

    if not interaction.permissions.administrator:
        await interaction.response.send_message("Hey! You can't run this command...", ephemeral=True)
        return False

    return True


async def is_magicarp(interaction: discord.Interaction) -> bool:
    """
    Check if the author of the command is magicarp37.

    :param interaction: The current :class:`discord.Interaction`
    :return: Is magicarp37
    """
    if not interaction.user.id == 662763830119628814:
        await interaction.response.send_message("Hey! You can't run this command...", ephemeral=True)
        return False

    return True
