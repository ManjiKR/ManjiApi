import aiohttp


class SkillData:
    def __init__(self):
        self.data_url = "https://raw.githubusercontent.com/ombe1229/yoshimitsu_frame_data/master/yoshimitsu_ko.json"

    @staticmethod
    async def get(url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                if r.status != 200:
                    return None
                return await r.json(content_type=None)

    async def get_all_skills(self):
        return await self.get(self.data_url)

    async def get_skill_by_num(self, num: int):
        resp = await self.get_all_skills()
        if len(resp) < num + 1:
            return

        return resp[num]
