(ns termproject
  (:use     [streamparse.specs])
  (:gen-class))

(defn termproject [options]
   [
    ;; spout configuration
    {"M-spout" (python-spout-spec
          options
          "spouts.messages.Messages"
          ["message"]
          )
    }
    ;; bolt configuration 1
    {"X-bolt" (python-bolt-spec
          options
          {"M-spout" :shuffle}
          "bolts.parsemessage.ParseMessage"
          ["measure"]
          )
    }
  ]
)
