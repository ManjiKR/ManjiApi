import aiohttp


class SkillData:
    def __init__(self):
        self.data_url = "https://raw.githubusercontent.com/ombe1229/yoshimitsu_frame_data/master/yoshimitsu_ko.json"

    @staticmethod
    async def request(url, **kwargs):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url, **kwargs) as r:
                if r.status != 200:
                    return None
                response = await r.json(content_type=None)
                return response

    async def get_all_skills(self):
        resp = await self.request(self.data_url)
        return resp

    async def get_skill_by_num(self, num: int):
        resp = await self.get_all_skills()
        try:
            info = resp[num]
        except IndexError:
            return None
        return info
