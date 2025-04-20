from database.models import init_db
from database.crud import add_fanfic

init_db()  # Make sure tables are created

add_fanfic(
    title="A Love Beyond Universes",
    author="Writer123",
    source="ao3",
    story_id="123456",
    filepath="storage/stories/ao3/Writer123/123456/story.html",
    summary="A story of time travel and love."
)
