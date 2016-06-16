describe("Click to Reveal XBlock", function() {

    var thumbs;
    var mockRuntime;
    var element;

    beforeEach(function() {

        // Install the HTML fixture for this test
        setFixtures('<div id="fixture">\n' +
                    '<span class="upvote"><span class="count">NOT UPDATED</span></span>\n' +
                    '<span class="downvote"><span class="count">NOT UPDATED</span></span>\n' +
                    '</div>');

        // Create a mock for the runtime
        mockRuntime = jasmine.createSpyObj('runtime', ['handlerUrl']);
        mockRuntime.handlerUrl.andCallFake(function() {
            return 'test url';
        });

        // Intercept POST requests through JQuery
        spyOn($, 'ajax').andCallFake(function(params) {
            // Call through to the success handler
            params.success({up:'test up', down:'test down'});
        });

        // Load the HTML fixture defined in the test runner
        element = $('#fixture').get();

        // Run the Click2RevealBlock script
        Click2RevealBlock(mockRuntime, element);
    });
});
