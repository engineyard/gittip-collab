# gittip-collab

Simple Gittip collaboration tool for teams.

## Why This Exists

At the moment, there is no way for a team to collaborate on a Gittip account. (Something Gittip [plans to fix](https://github.com/gittip/www.gittip.com/issues/1153).) John Resig [built a tool for Khan Academy](http://ejohn.org/blog/gittip-at-khan-academy/) that gives team members a tip allocation. Which is great, but his tool uses Google Docs. This tool does a similar thing, but the configuration is done with a YAML file.

## How To Configure It

Copy `sample.config.yaml` to `sample.config` and edit the file.

The sample config looks like this:

```yaml
account:
    username: "you"
    api_key: "SAMPLE"
    max_total: 60
tips:
    giver1:
        recipient1: 5
        recipient2: 15
    giver2:
        recipient3: 10
        recipient4: 10
    giver3:
        recipient2: 5
        recipient4: 5
        recipient5: 10
```

Set `username` to your team's Gittip account.

Set `api_key` to your API key, which can be found on your account dashboard.

Set `max_total` to the maximum weekly amount you want to give. It is split equally between team members. So if you specify `60` and you have three team members, each team member can tip a maximum of `20`.

Under `tips`, list your team members. These are for you internal use only, so `giver1` does not have to match up to anything on Gittip's side.

Each giver (i.e. team member) then lists recipients. These _do_ have to match up with Gittip, so `recipient1` should be the username of the person you want to tip.

You can specify as many tips as you like, as long as the total tip does not exceed the allowance for individual team members.

## How To Run It

Push configuration changes to Gittip by running `./update.py` from the CLI. This will replace all existing tips with the tips configured in the configuration file.

If there is a discrepancy in the amounts specified, the script will exit without updating anything.

If you try to tip someone who is not on Gittip, you will see an error message in the JSON that Gittip returns. Check this to make sure that everything looks okay.

It is not necessary to run `./update.py` in cron. It is sufficient to run it every time you make changes to the configuration file. If you keep this configuration file in Git, accountability is built in!
