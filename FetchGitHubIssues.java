import okhttp3.*;
import com.fasterxml.jackson.databind.*;

public class FetchGitHubIssues {
    private static final String GITHUB_API = "https://api.github.com";
    private static final String TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN";  // replace with your PAT
    private static final String OWNER = "octocat";                     // replace with repo owner
    private static final String REPO = "Hello-World";                  // replace with repo name

    public static void main(String[] args) throws Exception {
        OkHttpClient client = new OkHttpClient();
        ObjectMapper mapper = new ObjectMapper();

        String url = GITHUB_API + "/repos/" + OWNER + "/" + REPO + "/issues?state=all&per_page=100";
        Request request = new Request.Builder()
                .url(url)
                .header("Authorization", "Bearer " + TOKEN)
                .header("Accept", "application/vnd.github+json")
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("Request failed: " + response.code() + " - " + response.message());
                return;
            }

            String responseBody = response.body().string();
            JsonNode issues = mapper.readTree(responseBody);

            for (JsonNode issue : issues) {
                String title = issue.path("title").asText();
                String body = issue.path("body").asText();
                String createdAt = issue.path("created_at").asText();
                String author = issue.path("user").path("login").asText();
                int comments = issue.path("comments").asInt();
                String state = issue.path("state").asText();

                System.out.println("====================================");
                System.out.println("Title: " + title);
                System.out.println("Author: " + author);
                System.out.println("Created: " + createdAt);
                System.out.println("State: " + state);
                System.out.println("Comments: " + comments);
                System.out.println("Body:\n" + body);
                System.out.println("====================================\n");
            }
        }
    }
}
